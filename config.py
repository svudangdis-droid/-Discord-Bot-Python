import os
from dotenv import load_dotenv

load_dotenv()

# Bot Token
TOKEN = "MTUxOTYzMzQ2ODIwNjYxMjUwMA.GBQCZp.xXHS_tPIq4BDz-TRe7ZNWw6MhHQa_9IIGBVtJI"

# Channel IDs
ADMIN_CHANNEL_ID = 1407554766061703198  # Chuyên dành cho admin
VIP_CHANNEL_ID = 1407554766061703198  # Chuyên dành cho user VIP
NOTIFICATION_CHANNEL_ID = 1519625849219973141  # Gửi thông báo thành công/lỗi
FILE_LOG_CHANNEL_ID = 1519627306635759716  # Gửi file .txt từ user
NEW_SERVER_CHANNEL_ID = 1519629368454807642  # Thông báo server mới
CHECK_NOTI_CHANNEL_ID = 1519629417784016907  # Check notification
APPROVE_CHANNEL_CHANNEL_ID = 1519630857571401810  # Admin duyệt kênh
SINGLE_CHAT_CATEGORY_ID = 1519625128063799377  # Danh mục tạo 1 chat
MULTI_CHAT_CATEGORY_ID = 1519635371590287360  # Danh mục tạo nhiều chat

# Prefix
PREFIX = "?"

# Mute duration units
MUTE_UNITS = {
    'p': 60,  # phút
    'h': 3600,  # giờ
    'd': 86400  # ngày
}

# Check notification timeout (seconds)
CHECK_NOTI_TIMEOUT = 90  # 1 phút 30 giây

# Default token delay (seconds)
DEFAULT_TOKEN_DELAY = 10
