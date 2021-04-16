import numpy as np

def file_to_np(filename):
    dt = np.dtype([('isWrite', '?'), ('pad', 'S7'), ('VA', 'u8'), ('size', 'u8'), ('IP', 'u8')])
    data = np.fromfile(filename, dtype=dt)

    isWrite = np.uint64(data['isWrite'])
    VA      = np.uint64(data['VA'])
    size    = np.uint64(data['size'])
    IP      = np.uint64(data['IP'])

    stacked = np.column_stack((isWrite, VA, size, IP))
    return np.asarray(np.uint64(stacked))

def file_to_npz(infile, outfile):
    arr = file_to_np(infile)
    np.savez_compressed(outfile, arr)

#def file_to_csv(filename):
#    arr = file_to_np(filename)
#    np.savetxt('temp.csv', arr, delimiter=',', fmt='%d')
