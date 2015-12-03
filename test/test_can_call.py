import os
import subprocess
import init_all_test


ERROR_RES_MESSAGE = (
    "\033[031mERROR: Same name files exist in res directory\033[0m"
)


def create_res_file(filename, assert_string):
    with open(filename, 'w') as f:
        f.write(assert_string)


def delete_res_file(filename):
    os.remove(filename)


def test_call_in_res():
    filename = 'res/barkaerubar.txt'
    assert_string = 'This is res barkaerubar.txt'
    create_res_file(filename=filename, assert_string=assert_string)

    bin_out = subprocess.check_output(['./bin/boiler', 'barkaerubar'])

    os.chdir('bin')
    no_bin_out = subprocess.check_output(['./boiler', 'barkaerubar'])

    init_all_test.go_root()
    delete_res_file(filename=filename)
    assert bin_out == assert_string
    assert no_bin_out == assert_string


def test_call_in_res_local():
    filename = 'res_local/barkaerubar.txt'
    assert_string = 'This is res_local barkaerubar.txt'
    create_res_file(filename=filename, assert_string=assert_string)

    bin_out = subprocess.check_output(['./bin/boiler', 'barkaerubar'])

    os.chdir('bin')
    no_bin_out = subprocess.check_output(['./boiler', 'barkaerubar'])
    init_all_test.go_root()

    delete_res_file(filename=filename)
    assert bin_out == assert_string
    assert no_bin_out == assert_string


def test_is_error_call_colision():
    filename1 = 'res/barkaerubar.txt'
    filename2 = 'res/barkaerufoo.txt'
    assert_string1 = 'string1'
    assert_string2 = 'string2'
    create_res_file(filename=filename1, assert_string=assert_string1)
    create_res_file(filename=filename2, assert_string=assert_string2)

    def assert_error_mes(ex):
        assert ex.returncode == 1
        assert ex.output.split('\n') == [
            ERROR_RES_MESSAGE,
            'barkaerubar.txt',
            'barkaerufoo.txt',
            ''
        ]

    try:
        subprocess.check_output(['./bin/boiler', 'barkaeru'])
    except subprocess.CalledProcessError as ex:
        assert_error_mes(ex)

    os.chdir('bin')
    try:
        subprocess.check_output(['./boiler', 'barkaeru'])
    except subprocess.CalledProcessError as ex:
        assert_error_mes(ex)
    init_all_test.go_root()

    delete_res_file(filename=filename1)
    delete_res_file(filename=filename2)
