# Mapping of English letters to Standard Galactic Alphabet (SGA) characters
sga_mapping = {
    'A': 'ᔑ', 'B': 'ʖ', 'C': 'ᓵ', 'D': '↸', 'E': 'ᒷ', 'F': '⎓', 'G': '⊣', 'H': '⍑',
    'I': '╎', 'J': '⋮', 'K': 'ꖌ', 'L': 'ꖎ', 'M': 'ᒲ', 'N': 'リ', 'O': '𝙹', 'P': '!¡',
    'Q': 'ᑑ', 'R': '∷', 'S': 'ᓭ', 'T': 'ℸ', 'U': '⚍', 'V': '⍊', 'W': '∴', 'X': '̇/',
    'Y': '||', 'Z': '⨅'
}

def english_to_sga(text):
    # Convert each character in the text to its SGA equivalent
    sga_text = ''.join(sga_mapping.get(char.upper(), char) for char in text)
    return sga_text

# Example usage
english_text = "Hello World from MJTech46"
sga_text = english_to_sga(english_text)
print(f"Standard Galactic Alphabet: {sga_text}")
