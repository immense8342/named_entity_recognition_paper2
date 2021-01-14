from os.path import join
from codecs import open


def build_corpus(split, make_vocab=True, data_dir="./ResumeNER"):
    """读取数据"""
    assert split in ['train', 'dev', 'test']

    word_lists = []
    tag_lists = []
    with open(join(data_dir, split+"_BIOES.txt"), 'r', encoding='utf-8') as f:
        word_list = []
        tag_list = []
        for line in f:
            if line != '####EndOfBIOES####\r\n':
                print("split", split, "line", line,"line.strip('\\n').split()", line.strip('\n').split())
                if line.strip('\n') == "\r":
                    continue
                if len(line.strip('\n').split()) == 1:
                    word = " "
                    tag = line.strip('\n').split()[0]
                else:
                    word, tag = line.strip('\n').split()
                word_list.append(word)
                tag_list.append(tag)
            else:
                word_lists.append(word_list)
                tag_lists.append(tag_list)
                word_list = []
                tag_list = []

    # 如果make_vocab为True，还需要返回word2id和tag2id
    if make_vocab:
        word2id = build_map(word_lists)
        tag2id = build_map(tag_lists)
        print("tag_lists", tag_lists)
        print("tag2id", tag2id)
        return word_lists, tag_lists, word2id, tag2id
    else:
        return word_lists, tag_lists


def build_map(lists):
    maps = {}
    for list_ in lists:
        for e in list_:
            if e not in maps:
                maps[e] = len(maps)

    return maps
