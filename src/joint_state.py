import numpy as np

SAFE_LIMIT_RAD = 1.0


def analyze_joint_state(
    joint_angles: list[float],
    safe_limit_rad: float = SAFE_LIMIT_RAD,
) -> dict:
    """Analyze robot joint angles and return safety information."""
    angles = np.asarray(joint_angles, dtype=float)

    if angles.ndim != 1:
        raise ValueError("joint_angles must be a one-dimensional sequence")

    if angles.size == 0:
        raise ValueError("joint_angles cannot be empty")

    unsafe_mask = np.abs(angles) > safe_limit_rad
    unsafe_joint_numbers = np.where(unsafe_mask)[0] + 1

    return {
        "joint_count": int(angles.size),
        "mean_angle_rad": float(angles.mean()),
        "unsafe_joint_numbers": unsafe_joint_numbers.tolist(),
    }


def main() -> None:
    demo_joint_angles = [0.0, 0.5, -0.3, 1.2, 0.1, 0.0]
    result = analyze_joint_state(demo_joint_angles)

    print(f"Joint count: {result['joint_count']}")
    print(f"Mean angle: {result['mean_angle_rad']:.2f} rad")
    print(f"Unsafe joints: {result['unsafe_joint_numbers']}")


if __name__ == "__main__":
    main()