def main(s1,s2,s3):
    """
    Given three strings, s1, s2 and s3. return their odd lengths, example "[s1, s2]". If there is no odd length, return "[]".
    Args:
        s1: string
        s2: string
        s3: string
    Returns:
        string
    """
    s1="codeschool.uz" 
    s2="example" 
    s3="python"
    odd_length_strings = []
    if len(s1) % 2 == 1:
        odd_length_strings.append(s1)
    if len(s2) % 2 == 1:
        odd_length_strings.append(s2)
    if len(s3) % 2 == 1:
        odd_length_strings.append(s3)
    if len(odd_length_strings) == 0:
        return "[]"
    else:
        return str(odd_length_strings)