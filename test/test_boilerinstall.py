import os
import subprocess
import init_all_test


# clone test directory
root = os.getcwd()
os.chdir('test')
subprocess.call(['git', 'clone', root, 'module/KaeruBoilerplate'])

init_all_test.go_root()


def create_kaeru_package():
    kaeru_package = (
        '{{"kaeru_test": "{root}/test/module/KaeruBoilerplate"}}'
        .format(root=root)
    )
    subprocess.call(
        ['mv', 'kaeru_package.json', 'test/tmp_kaeru_package.json'])
    with open('kaeru_package.json', 'w') as f:
        f.write(kaeru_package)


def test_set_boilerinstall():
    create_kaeru_package()
    result = subprocess.check_output(['bin/boilerinstall'])
    assert result.split('\n') == [
        (
            "\033[032mINFO: This package [{}] is installed!!\033[0m"
            .format("kaeru_test")
        ),
        "\033[032mINFO: All tasks are done.\033[0m",
        ''
    ]

    result = subprocess.check_output(['bin/boilerinstall'])
    assert result.split('\n') == [
        "Already up-to-date.",
        (
            "\033[033mINFO: This package [{}] was already installed."
            " Updating is called.\033[0m"
            .format("kaeru_test")
        ),
        "\033[032mINFO: All tasks are done.\033[0m",
        ''
    ]


def teardown_function(func):
    subprocess.call(
        ['mv', 'test/tmp_kaeru_package.json', 'kaeru_package.json'])
    subprocess.call(['rm', '-rf', 'res/kaeru_test'])
    subprocess.call(['rm', '-rf', 'test/module/KaeruBoilerplate'])
