def get_skus_from_txt():
    # file = open(r'F:\Work\Document\选品\选品.txt')
    file = open(r'F:\Work\Doc\选品\up_recommand.txt')
    lines = file.readlines()
    skus = ""
    for line in lines:
        line = line.strip('\n')
        skus = skus + "," + line
    print(skus[1:])


if __name__ == '__main__':
    get_skus_from_txt()
