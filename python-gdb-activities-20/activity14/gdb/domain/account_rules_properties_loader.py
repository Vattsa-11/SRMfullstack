# gdb/domain/account_rules_properties_loader.py
import os

class AccountRulesPropertiesLoader:
    """Utility loading external .properties files."""

    @staticmethod
    def load_rules(account_type: str) -> dict:
        # TODO (Step 2): Load gdb/resources/config/rules/<account_type in lower case>.properties into a dict.
        #   1. Build the path relative to this module so it works from any working directory, e.g.
        #      os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "resources", "config", "rules", ...)
        #   2. If the file does not exist, return an empty dict.
        #   3. Read it line by line (encoding="utf-8"); skip blank lines and lines starting with "#".
        #   4. Split each remaining "key=value" line on the FIRST "=" and store the stripped key and value strings.

        rules = {}
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "resources", "config", "rules", f"{account_type.lower()}.properties")
        if not os.path.exists(file_path):
            return rules

        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                key, value = line.split("=", 1)
                rules[key.strip()] = value.strip()

        return rules
    
        raise NotImplementedError("TODO: implement AccountRulesPropertiesLoader.load_rules()")
