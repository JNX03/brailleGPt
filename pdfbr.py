import PyPDF2

# Braille alphabet mapping including English (uppercase and lowercase), numbers, and some punctuation
braille_map = {
    'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑', 'f': '⠋', 'g': '⠛', 'h': '⠓',
    'i': '⠊', 'j': '⠚', 'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕', 'p': '⠏',
    'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞', 'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭',
    'y': '⠽', 'z': '⠵', 'A': '⠠⠁', 'B': '⠠⠃', 'C': '⠠⠉', 'D': '⠠⠙', 'E': '⠠⠑',
    'F': '⠠⠋', 'G': '⠠⠛', 'H': '⠠⠓', 'I': '⠠⠊', 'J': '⠠⠚', 'K': '⠠⠅', 'L': '⠠⠇',
    'M': '⠠⠍', 'N': '⠠⠝', 'O': '⠠⠕', 'P': '⠠⠏', 'Q': '⠠⠟', 'R': '⠠⠗', 'S': '⠠⠎',
    'T': '⠠⠞', 'U': '⠠⠥', 'V': '⠠⠧', 'W': '⠠⠺', 'X': '⠠⠭', 'Y': '⠠⠽', 'Z': '⠠⠵',
    '0': '⠼⠚', '1': '⠼⠁', '2': '⠼⠃', '3': '⠼⠉', '4': '⠼⠙', '5': '⠼⠑', '6': '⠼⠋',
    '7': '⠼⠛', '8': '⠼⠓', '9': '⠼⠊', ' ': ' ', '\n': '\n', ',': '⠂', '.': '⠲', '?': '⠦',
    '!': '⠖', ';': '⠆', ':': '⠒', '-': '⠤', '(': '⠶', ')': '⠶', '/': '⠌', '\'': '⠄', '\"': '⠘',
    '฿': '⠸⠃', 'ก': '⠁', 'ข': '⠃', 'ฃ': '⠉', 'ค': '⠙', 'ฅ': '⠑', 'ฆ': '⠋', 'ง': '⠛', 
    'จ': '⠓', 'ฉ': '⠊', 'ช': '⠚', 'ซ': '⠅', 'ฌ': '⠇', 'ญ': '⠍', 'ฎ': '⠝', 'ฏ': '⠕', 
    'ฐ': '⠏', 'ฑ': '⠟', 'ฒ': '⠗', 'ณ': '⠎', 'ด': '⠞', 'ต': '⠥', 'ถ': '⠧', 'ท': '⠺', 
    'ธ': '⠭', 'น': '⠽', 'บ': '⠵', 'ป': '⠷', 'ผ': '⠾', 'ฝ': '⠮', 'พ': '⠤', 'ฟ': '⠸', 
    'ภ': '⠊', 'ม': '⠫', 'ย': '⠻', 'ร': '⠘', 'ฤ': '⠙', 'ล': '⠛', 'ฦ': '⠇', 'ว': '⠾', 
    'ศ': '⠓', 'ษ': '⠊', 'ส': '⠚', 'ห': '⠅', 'ฬ': '⠇', 'อ': '⠍', 'ฮ': '⠝', 'ฯ': '⠕', 
    'ะ': '⠏', 'ั': '⠟', 'า': '⠗', 'ำ': '⠎', 'ิ': '⠞', 'ี': '⠥', 'ึ': '⠧', 'ื': '⠺', 
    'ุ': '⠭', 'ู': '⠽', 'ฺ': '⠵', '฻': '⠷', '฼': '⠾', '฽': '⠮', '฾': '⠤', '฿': '⠸', 
    'เ': '⠘', 'แ': '⠫', 'โ': '⠻', 'ใ': '⠘', 'ไ': '⠙'
}

def text_to_braille(text):
    braille_text = ''.join(braille_map.get(char, '?') for char in text)
    return braille_text

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

def main():
    pdf_path = input("Enter the path of the PDF file: ")
    text = extract_text_from_pdf(pdf_path)
    braille_text = text_to_braille(text)
    output_path = pdf_path.replace('.pdf', '_braille.txt')
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(braille_text)
    print(f"Braille text saved to {output_path}")

if __name__ == "__main__":
    main()
