import os
import tempfile

class Config:
    # Flask 配置
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'viswords-secret-key-2025'
    FLASK_ENV = os.environ.get('FLASK_ENV') or 'development'
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG') == 'true'
    
    # 豆包API配置
    ARK_API_KEY = os.environ.get('ARK_API_KEY') or "您的豆包API密钥"
    DOUBAO_API_URL = os.environ.get('DOUBAO_API_URL') or "https://ark.cn-beijing.volces.com/api/v3"
    DOUBAO_MODEL = os.environ.get('DOUBAO_MODEL') or "doubao-seed-1-6-lite-251015"
    AI_TEMPERATURE = float(os.environ.get('AI_TEMPERATURE') or '0.7')
    
    # 数据库配置 - 在Vercel环境中使用临时目录
    if os.environ.get('VERCEL'):
        DATABASE = os.path.join(tempfile.gettempdir(), 'viswords.db')
        UPLOAD_FOLDER = os.path.join(tempfile.gettempdir(), 'uploads')
    else:
        DATABASE = os.environ.get('DATABASE') or 'viswords.db'
        UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER') or 'uploads'
    
    # 文件上传配置
    MAX_CONTENT_LENGTH = int(os.environ.get('MAX_CONTENT_LENGTH') or '16777216')  # 16MB
    ALLOWED_EXTENSIONS = set(os.environ.get('ALLOWED_EXTENSIONS', 'png,jpg,jpeg,gif').split(','))
    
    # 学习配置
    DEFAULT_LEVEL = os.environ.get('DEFAULT_LEVEL') or 'CET-4'
    DAILY_WORD_LIMIT = int(os.environ.get('DAILY_WORD_LIMIT') or '50')
    REVIEW_INTERVAL_DAYS = int(os.environ.get('REVIEW_INTERVAL_DAYS') or '7')
    
    @staticmethod
    def init_app(app):
        # 确保上传目录存在
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
