import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))


class ImportResolutionTests(unittest.TestCase):
    def test_streamlit_and_agent_module_are_available(self):
        import streamlit  # noqa: F401
        from agent import run_agent  # noqa: F401

        self.assertTrue(callable(run_agent))


if __name__ == "__main__":
    unittest.main()
