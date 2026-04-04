from typing import List

from src.checks import BaseCheck


class Reporter():
    def __init__(self, checks: List[BaseCheck]):
        self.checks = checks

    def report(self):
        for check in self.checks:
            print(f"Host name: {check.host.name}, check type: {type(check).__name__}, check result: {check.result}")