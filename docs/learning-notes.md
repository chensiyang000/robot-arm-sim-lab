# Robot Arm Sim Lab 学习笔记

> 目标岗位：机器人软件工程师实习生 / 具身智能算法工程化方向。
>
> 本项目目标：在 GitHub 上完成一个基于 Python 与 MuJoCo 的机械臂仿真、控制、数据记录与策略训练项目。

## 1. 当前环境

- 操作系统：Windows
- 显卡：NVIDIA GeForce RTX 3060，6GB 显存
- 内存：16GB
- Python：3.14.4
- Git：已安装并可在 PowerShell 使用

### 环境结论

当前电脑适合学习 Python、Git、NumPy、MuJoCo 基础仿真和轻量模型训练。

ROS2、Docker、真机驱动和完整 Isaac Sim 工作流后续在 Ubuntu 中学习。由于显存和内存有限，Isaac Sim 以极简场景熟悉工作流为主，主要仿真项目使用 MuJoCo。

## 2. 已完成的工具与操作

### 2.1 Git 安装与配置

已在 Windows 上安装 Git，并完成全局身份配置。

常用命令：

```powershell
git --version
git config --global --list
```

- `git --version`：检查 Git 是否安装成功。
- `git config --global --list`：查看当前 Git 用户配置。

### 2.2 第一个本地 Git 仓库

创建了本地学习目录，并学习了以下命令：

```powershell
git init
git status
git add src
git commit -m "提交说明"
git log --oneline
```

- `git init`：初始化一个本地 Git 仓库。
- `git status`：查看文件是否被 Git 跟踪、是否有改动未提交。
- `git add`：把修改放入暂存区，准备提交。
- `git commit`：创建一个本地版本记录。
- `git log --oneline`：用一行查看每次提交的历史。

## 3. Python 基础：机器人关节状态

完成了两个 Python 练习文件：

- `hello_robot.py`：保存和输出机械臂名称、关节角度与平均角度。
- `joint_check.py`：逐个检查关节角度是否超出安全范围。

### 3.1 关键概念

```python
joint_angles = [0.0, 0.5, -0.3, 1.2, 0.1, 0.0]
```

这是一台六轴机械臂的关节角度列表。

- Python 列表从 `0` 开始编号。
- 第 1 个关节：`joint_angles[0]`。
- 第 3 个关节：`joint_angles[2]`。
- 第 6 个关节：`joint_angles[5]`。

常用函数：

```python
len(joint_angles)       # 关节数量
sum(joint_angles)       # 所有关节角度相加
abs(angle)              # 取绝对值
```

### 3.2 安全检查逻辑

```python
safe_limit = 1.0

for index, angle in enumerate(joint_angles):
    joint_number = index + 1
    if abs(angle) <= safe_limit:
        print(f"关节 {joint_number}: 状态正常")
    else:
        print(f"关节 {joint_number}: 超出安全范围！")
```

含义：依次检查每个关节角度是否在 `-1.0` 到 `1.0` 弧度之间。练习数据中第 4 个关节为 `1.20 rad`，因此超出范围。

## 4. GitHub 项目

已创建 GitHub 仓库：`robot-arm-sim-lab`。

本地项目目录结构：

```text
robot-arm-sim-lab/
├── assets/     # 图片、演示材料
├── data/       # 本地仿真数据，不提交到 GitHub
├── docs/       # 技术文档和学习笔记
├── src/        # Python 源代码
├── tests/      # 自动测试
└── README.md   # GitHub 项目主页
```

### 4.1 GitHub 仓库操作

```powershell
git clone <仓库地址>
cd robot-arm-sim-lab
```

- `git clone`：将 GitHub 远程仓库复制到本地。
- `cd`：切换到项目目录。

## 5. NumPy 机械臂关节分析

项目已创建独立虚拟环境 `.venv`，并安装 NumPy：

```powershell
python -m pip install numpy
python -m pip freeze > requirements.txt
```

- `python -m pip install numpy`：在当前项目的虚拟环境中安装 NumPy。
- `python -m pip freeze > requirements.txt`：将已安装库及版本写入依赖清单，便于他人复现实验环境。

第一个项目源文件为 `src/joint_state.py`。它使用 NumPy 数组同时处理六个关节角度：

```python
unsafe_mask = np.abs(joint_angles) > SAFE_LIMIT_RAD
unsafe_joint_numbers = np.where(unsafe_mask)[0] + 1
```

- `np.abs`：同时计算所有关节角度的绝对值。
- 比较运算：同时判断所有关节是否超过安全阈值。
- `np.where`：找出值为真的数组位置。
- `+ 1`：将从 0 开始的 Python 下标转换为机械臂的第 1、2、3 个关节编号。

当前测试结果：6 个关节的平均角度为 `0.25 rad`，第 4 个关节的角度为 `1.20 rad`，超过 `1.0 rad` 的安全限制。

## 6. 项目路线图

1. 配置 Python 虚拟环境，安装 NumPy。
2. 用 NumPy 处理关节向量、位姿与三维坐标。
3. 安装并运行第一个 MuJoCo 机械臂仿真。
4. 编写轨迹控制与关节安全控制。
5. 记录仿真轨迹，构建数据集。
6. 实现并评测一个简单模仿学习策略。
7. 在 Ubuntu 中学习 Docker、ROS2，并接入机器人工作流。
8. 完善 README、演示视频和简历项目描述。

## 7. 复习问题

1. 为什么 Python 列表的第 3 个元素写作 `list[2]`？
2. `git add` 和 `git commit` 分别做什么？
3. 为什么机器人控制程序需要设置关节安全范围？
4. 为什么大型数据集和 Python 虚拟环境不应直接提交到 GitHub？
5. MuJoCo 在本项目中承担什么作用？
6. `np.where(unsafe_mask)[0] + 1` 为什么最终得到 `[4]`？

## 8. 下一步

下一课：安装 NumPy，并学习如何用数组表示机械臂关节向量和末端三维坐标。
