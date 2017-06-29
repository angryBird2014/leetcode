import numpy as np


def pearson_correlation(object1, object2):
    values = range(len(object1))

    # Summation over all attributes for both objects
    sum_object1 = sum([float(object1[i]) for i in values])
    sum_object2 = sum([float(object2[i]) for i in values])

    # Sum the squares
    square_sum1 = sum([pow(object1[i], 2) for i in values])
    square_sum2 = sum([pow(object2[i], 2) for i in values])

    # Add up the products
    product = sum([object1[i] * object2[i] for i in values])

    # Calculate Pearson Correlation score
    numerator = product - (sum_object1 * sum_object2 / len(object1))
    denominator = ((square_sum1 - pow(sum_object1, 2) / len(object1)) * (square_sum2 -
                                                                         pow(sum_object2, 2) / len(object1))) ** 0.5

    # Can"t have division by 0
    if denominator == 0:
        return 0

    result = numerator / denominator
    return result

if __name__ == '__main__':
    v1 = '1111111100'
    v1 = [int(i) for i in v1]
    v2 = '1111111100'
    v2 = [int(i) for i in v2]
    v3 = '1011111100'
    v3 = [int(i) for i in v3]

    print(pearson_correlation(v2, v3))

    v4 = '1111111100'
    v4 = [int(i) for i in v4]
    v5 = '0111011101'
    v5 = [int(i) for i in v5]
    v6 = '1000101111'
    v6 = [int(i) for i in v6]

    print(pearson_correlation(v5, v6))