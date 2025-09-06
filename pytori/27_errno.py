import errno
print(f"errno.EPERM: {errno.EPERM}")  # 1   (Operation not permitted)
print(f"errno.ENOENT: {errno.ENOENT}")  # 2   (No such file or directory)
print(f"errno.ESRCH: {errno.ESRCH}")    # 3   (No such process)
print(f"errno.EINTR: {errno.EINTR}")    # 4   (Interrupted system call)
print(f"errno.EIO: {errno.EIO}")      # 5   (I/O error)
print(f"errno.ENXIO: {errno.ENXIO}")    # 6   (No such device or address) 