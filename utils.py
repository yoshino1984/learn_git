#!/usr/bin/env python3
"""
工具函数模块
"""

def greet(name):
    """问候函数"""
    return f"你好, {name}!"


def calculate(a, b, operation="add"):
    """
    简单的计算器函数

    Args:
        a: 第一个数字
        b: 第二个数字
        operation: 运算类型 (add, subtract, multiply, divide)

    Returns:
        计算结果
    """
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            raise ValueError("除数不能为零")
        return a / b
    else:
        raise ValueError(f"不支持的运算: {operation}")
