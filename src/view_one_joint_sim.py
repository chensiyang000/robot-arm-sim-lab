from pathlib import Path
import time

import mujoco
import mujoco.viewer


MODEL_PATH = Path(__file__).parent.parent / "models" / "one_joint_arm.xml"
INITIAL_ANGLE_RAD = 0.8
DISPLAY_DURATION_SECONDS = 30.0


def main() -> None:
    model = mujoco.MjModel.from_xml_path(str(MODEL_PATH))
    data = mujoco.MjData(model)

    data.qpos[0] = INITIAL_ANGLE_RAD
    mujoco.mj_forward(model, data)

    with mujoco.viewer.launch_passive(model, data) as viewer:
        viewer.cam.azimuth = 135.0
        viewer.cam.elevation = -25.0
        viewer.cam.distance = 2.5
        viewer.cam.lookat[:] = [0.0, 0.0, 0.75]
        viewer.sync()

        while viewer.is_running() and data.time < DISPLAY_DURATION_SECONDS:
            mujoco.mj_step(model, data)
            viewer.sync()
            time.sleep(model.opt.timestep)


if __name__ == "__main__":
    main()
