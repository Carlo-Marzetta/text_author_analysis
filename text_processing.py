

from pathlib import Path
import re



class TextFileProcessor:
    def __init__(self, directory: Path) -> None:
        self.directory = directory

    def process(self) -> dict[Path, list[str]]:
        results = {}

        for file_path in sorted(self.directory.glob("*.txt")):
            text = file_path.read_text(encoding="utf-8")
            results[file_path] = self.tokenize(text)

        return results
        
    def tokenize(self, text: str) -> list[str]:
        text = text.lower()

        # Elimina i punti
        text = text.replace(".", " ")

        # Normalizza gli spazi
        text = re.sub(r"\s+", " ", text).strip()

        # Mantiene i token strutturali <...> e le parole con apostrofi e trattini
        tokens = re.findall(r"<[^>]+>|[\w'-]+", text)

        # Elimina i token composti solo da cifre
        return [token for token in tokens if re.fullmatch(r"\d+", token) is None]