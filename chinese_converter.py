"""
ComfyUI Traditional Chinese to Simplified Chinese Converter Node
繁體中文轉簡體中文節點

安裝依賴：
pip install opencc-python-reimplemented
"""

class TraditionalToSimplifiedChinese:
    """
    將繁體中文文本轉換為簡體中文
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {
                    "multiline": True,
                    "default": "請輸入繁體中文文字"
                }),
            },
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("simplified_text",)
    FUNCTION = "convert"
    CATEGORY = "text/chinese"
    
    def convert(self, text):
        try:
            from opencc import OpenCC
            
            # 創建繁體轉簡體的轉換器
            cc = OpenCC('t2s')  # t2s = Traditional to Simplified
            
            # 執行轉換
            simplified = cc.convert(text)
            
            return (simplified,)
        
        except ImportError:
            error_msg = "錯誤：未安裝 opencc-python-reimplemented\n請執行：pip install opencc-python-reimplemented"
            print(error_msg)
            return (error_msg,)
        
        except Exception as e:
            error_msg = f"轉換錯誤：{str(e)}"
            print(error_msg)
            return (error_msg,)


class SimplifiedToTraditionalChinese:
    """
    將簡體中文文本轉換為繁體中文（額外功能）
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {
                    "multiline": True,
                    "default": "请输入简体中文文字"
                }),
            },
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("traditional_text",)
    FUNCTION = "convert"
    CATEGORY = "text/chinese"
    
    def convert(self, text):
        try:
            from opencc import OpenCC
            
            # 創建簡體轉繁體的轉換器
            cc = OpenCC('s2t')  # s2t = Simplified to Traditional
            
            # 執行轉換
            traditional = cc.convert(text)
            
            return (traditional,)
        
        except ImportError:
            error_msg = "错误：未安装 opencc-python-reimplemented\n请执行：pip install opencc-python-reimplemented"
            print(error_msg)
            return (error_msg,)
        
        except Exception as e:
            error_msg = f"转换错误：{str(e)}"
            print(error_msg)
            return (error_msg,)


# ComfyUI 節點註冊
NODE_CLASS_MAPPINGS = {
    "TraditionalToSimplifiedChinese": TraditionalToSimplifiedChinese,
    "SimplifiedToTraditionalChinese": SimplifiedToTraditionalChinese,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TraditionalToSimplifiedChinese": "繁體轉簡體 (Traditional to Simplified)",
    "SimplifiedToTraditionalChinese": "簡體轉繁體 (Simplified to Traditional)",
}