class TokenTransformer:

    def __init__(self, tokens: list[str]) -> None:
        self.tokens = tokens.copy()


    def remove_tokens(self, to_remove: set[str]) -> list[str]:
        self.tokens = [token for token in self.tokens if token not in to_remove]
        return self.tokens.copy()

    def replace_tokens(self, mapping: dict[str, str]) -> list[str]:
        self.tokens = [mapping.get(token, token) for token in self.tokens]
        return self.tokens.copy()

    def transform(self) -> list[str]:

        mapping = {
            "<nl>": "<break>",
            "<par>": "<break>",
        }

        self.replace_tokens(mapping)
        return self.merge_breaks()