#!/usr/bin/env python3
"""
Antigravity Tools API 测试脚本
测试 OpenAI 兼容的 API 端点
"""

import openai
import sys

def test_basic_request():
    """测试基础请求"""
    print("=" * 60)
    print("测试 1: 基础请求（非流式）")
    print("=" * 60)
    
    try:
        client = openai.OpenAI(
            api_key="sk-7fd8d437a64b4bf8b011fb17945a109d",
            base_url="http://127.0.0.1:8045/v1"
        )
        
        response = client.chat.completions.create(
            model="gemini-3-flash",
            messages=[{"role": "user", "content": "用一句话介绍你自己"}],
            max_tokens=100
        )
        
        print(f"✅ 请求成功！")
        print(f"模型: {response.model}")
        print(f"回复: {response.choices[0].message.content}")
        print(f"Token 使用: {response.usage.total_tokens if response.usage else 'N/A'}")
        return True
        
    except Exception as e:
        print(f"❌ 请求失败: {e}")
        return False

def test_streaming_request():
    """测试流式请求"""
    print("\n" + "=" * 60)
    print("测试 2: 流式请求")
    print("=" * 60)
    
    try:
        client = openai.OpenAI(
            api_key="sk-7fd8d437a64b4bf8b011fb17945a109d",
            base_url="http://127.0.0.1:8045/v1"
        )
        
        stream = client.chat.completions.create(
            model="gemini-3-flash",
            messages=[{"role": "user", "content": "数到5"}],
            stream=True
        )
        
        print("✅ 流式响应开始:")
        print("回复: ", end="", flush=True)
        
        for chunk in stream:
            if chunk.choices[0].delta.content:
                print(chunk.choices[0].delta.content, end="", flush=True)
        
        print("\n✅ 流式请求完成！")
        return True
        
    except Exception as e:
        print(f"❌ 流式请求失败: {e}")
        return False

def test_multi_turn():
    """测试多轮对话"""
    print("\n" + "=" * 60)
    print("测试 3: 多轮对话")
    print("=" * 60)
    
    try:
        client = openai.OpenAI(
            api_key="sk-7fd8d437a64b4bf8b011fb17945a109d",
            base_url="http://127.0.0.1:8045/v1"
        )
        
        messages = [
            {"role": "user", "content": "我的名字是小明"},
            {"role": "assistant", "content": "你好，小明！很高兴认识你。"},
            {"role": "user", "content": "我刚才说我叫什么？"}
        ]
        
        response = client.chat.completions.create(
            model="gemini-3-flash",
            messages=messages,
            max_tokens=50
        )
        
        print(f"✅ 多轮对话成功！")
        print(f"回复: {response.choices[0].message.content}")
        return True
        
    except Exception as e:
        print(f"❌ 多轮对话失败: {e}")
        return False

def main():
    print("\n🚀 Antigravity Tools API 测试")
    print(f"API 端点: http://127.0.0.1:8045/v1")
    print(f"API 密钥: sk-7fd8d437a64b4bf8b011fb17945a109d")
    print()
    
    results = []
    
    # 运行测试
    results.append(("基础请求", test_basic_request()))
    results.append(("流式请求", test_streaming_request()))
    results.append(("多轮对话", test_multi_turn()))
    
    # 总结
    print("\n" + "=" * 60)
    print("测试总结")
    print("=" * 60)
    
    for name, success in results:
        status = "✅ 通过" if success else "❌ 失败"
        print(f"{name}: {status}")
    
    total = len(results)
    passed = sum(1 for _, success in results if success)
    
    print(f"\n总计: {passed}/{total} 测试通过")
    
    if passed == total:
        print("\n🎉 所有测试通过！Antigravity 代理服务运行正常。")
        sys.exit(0)
    else:
        print("\n⚠️ 部分测试失败，请检查 Antigravity 服务状态。")
        sys.exit(1)

if __name__ == "__main__":
    main()
