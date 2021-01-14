# 设置lstm训练参数
class TrainingConfig(object):
    batch_size = 1
    # 学习速率
    lr = 0.001
    epoches = 30
    print_step = 5


class LSTMConfig(object):
    emb_size = 96  # 词向量的维数
    hidden_size = 96  # lstm隐向量的维数
