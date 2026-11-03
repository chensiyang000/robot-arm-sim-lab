import unittest

from src.joint_state import analyze_joint_state


class TestAnalyzeJointState(unittest.TestCase):
    def test_all_joints_safe(self) -> None:
        result = analyze_joint_state([0.0, 0.2, -0.4])

        self.assertEqual(result["joint_count"], 3)
        self.assertEqual(result["unsafe_joint_numbers"], [])
        self.assertAlmostEqual(result["mean_angle_rad"], -0.0666666667)

    def test_detects_unsafe_joint(self) -> None:
        result = analyze_joint_state([0.0, 1.2, -1.5])

        self.assertEqual(result["unsafe_joint_numbers"], [2, 3])

    def test_empty_joint_state_raises_error(self) -> None:
        with self.assertRaises(ValueError):
            analyze_joint_state([])


if __name__ == "__main__":
    unittest.main()