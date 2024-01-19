from nguylinc_python_utils.misc import run_command

mobi_path = "test.mobi"
txt_path = "test.txt"
run_command(f'ebook-convert "{mobi_path}" "{txt_path}"')
