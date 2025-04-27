# log.py
import logging
from logging.handlers import RotatingFileHandler
import os


def setup_logger(name, log_file, level=logging.INFO, file_size=5*1024*1024, backup_count=5):
    """
    创建一个日志记录器并设置其输出格式、文件大小和备份文件数量

    Args:
        name (str): 日志记录器的名字
        log_file (str): 日志文件的路径
        level (int): 日志级别，默认为INFO
        file_size (int): 日志文件的最大大小，默认为5MB
        backup_count (int): 最多保留的备份文件数量，默认为5

    Returns:
        logger: 配置好的日志记录器对象
    """
    # 创建日志目录（如果不存在）
    log_dir = os.path.dirname(log_file)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # 创建一个日志记录器
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # 创建一个文件处理器，使用RotatingFileHandler来限制日志文件的大小
    # 当日志文件超过指定大小时，会自动旋转日志文件
    file_handler = RotatingFileHandler(
        log_file, maxBytes=file_size, backupCount=backup_count
    )
    file_handler.setLevel(level)

    # 创建一个控制台处理器，用于将日志输出到控制台
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)

    # 创建日志格式
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # 添加处理器到日志记录器
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


# 以下是示例代码，展示如何使用上述日志模块
if __name__ == "__main__":
    # 实例化日志记录器
    my_logger = setup_logger('my_logger', 'app.log')

    # 记录不同级别的日志
    my_logger.debug("这是一个调试信息")
    my_logger.info("这是一个信息消息")
    my_logger.warning("这是一个警告消息")
    my_logger.error("这是一个错误消息")
    my_logger.critical("这是一个严重错误消息")