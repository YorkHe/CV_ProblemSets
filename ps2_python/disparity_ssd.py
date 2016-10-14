import numpy as np

def disparity_ssd(L, R):
    """Compute disparity map D(y, x) such that: L(y, x) = R(y, x + D(y, x))

    Params:
    L: Grayscale left image
    R: Grayscale right image, same size as L

    Returns: Disparity map, same size as L, R
    """

    col_num, row_num = L.shape
    tplCols, tplRows = R.shape
    hf_tplCols = tplCols / 2
    hf_tplRows = tplRows / 2

    S = np.zeros((col_num, row_num))
    iter_sum = 0;
    RR = 0;

    print col_num, row_num



    for r in range (col_num):
        iter_sum = 0
        for c in range (row_num):
            for i in range (tplCols):
                for j in range (tplRows):
                    if (r + i < hf_tplCols or r + i >= 3 * hf_tplCols or
                        c + j < hf_tplRows or c + j >= 3 * hf_tplRows):
                        RR = 0;
                    else:
                        RR = R[r + i - hf_tplCols, c + j - hf_tplRows]
                    iter_sum += pow(L[i,j] - RR, 2)

        S[r,c] = iter_sum

    return S
