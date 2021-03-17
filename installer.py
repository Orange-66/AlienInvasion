import os


# 将此项目转换成exe文件
def project_to_exe(project_name="Alien_Invasion"):
    # 打包项目
    cmd = 'pyinstaller -F -w ' \
          './alien_invasion.py ' \
          '--workpath ./EXE/ ' \
          '--specpath ./EXE/ ' \
          '--distpath ./EXE/ ' \
          '--name {project_name} ' \
          '--clean '.format(project_name=project_name)

    os.system(cmd)

    # 删除spec文件
    root_dir = "./EXE/"
    spec_filename = "Alien_Invasion.spec"
    if os.path.exists(os.path.join(root_dir, spec_filename)):
        os.remove(os.path.join(root_dir, spec_filename))
    else:
        print(f'没有找到 [{os.path.join(root_dir, spec_filename)}] 文件或文件夹')

    # 删除workspace文件夹
    root_dir = "./EXE/Alien_Invasion/"
    if os.path.exists(root_dir):
        files = os.listdir(root_dir)
        for filename in files:
            if os.path.exists(os.path.join(root_dir, filename)):
                os.remove(os.path.join(root_dir, filename))

        os.rmdir(root_dir)
    else:
        print(f'没有找到 [{root_dir}] 文件或文件夹')


if __name__ == "__main__":
    project_to_exe()
