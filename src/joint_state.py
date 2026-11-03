import numpy as np

SAFE_LIMIT_RAD = 1.0

joint_angles = np.array(
    [0.0, 0.5, -0.3, 1.2, 0.1, 0.0],
    dtype=float,
)

unsafe_mask = np.abs(joint_angles) > SAFE_LIMIT_RAD
unsafe_joint_numbers = np.where(unsafe_mask)[0] + 1

print(f"Joint count: {joint_angles.size}")
print(f"Mean angle: {joint_angles.mean():.2f} rad")
print(f"Unsafe joints: {unsafe_joint_numbers.tolist()}")