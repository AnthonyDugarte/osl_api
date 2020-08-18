import time
import re



def remove_leading_slash(s: str):
    return re.search(r"^\/?(.*)", s, re.M).group(1)


def gen_osl_tonce():
    return str(int(time.time() * 1e6))
