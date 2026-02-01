import yt_dlp
import os


def download_audio(url, output_path='downloads'):
    """
    YouTubeのURLから音声のみを抽出してダウンロードする

    Args:
        url (str): YouTubeの動画URL
        output_path (str): 保存先ディレクトリ（デフォルト: 'downloads'）
    """
    # 保存先ディレクトリが存在しない場合は作成
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # yt-dlpのオプション設定
    ydl_opts = {
        'format': 'bestaudio/best',  # 最高品質の音声を取得
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # 音声抽出
            'preferredcodec': 'mp3',      # MP3形式に変換
            'preferredquality': '192',    # ビットレート192kbps
        }],
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),  # 出力ファイル名
        'quiet': False,  # 進捗を表示
        'no_warnings': False,
        # 403エラー対策
        'extractor_args': {
            'youtube': {
                'player_client': ['android', 'web'],
                'player_skip': ['webpage', 'configs'],
            }
        },
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-us,en;q=0.5',
            'Sec-Fetch-Mode': 'navigate',
        },
        # Cookieを使用（オプション）
        'cookiefile': None,  # 必要に応じてCookieファイルのパスを指定
    }

    try:
        print(f"ダウンロード開始: {url}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # 動画情報を取得
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            # 拡張子をmp3に変更
            base = os.path.splitext(filename)[0]
            audio_file = f"{base}.mp3"
            print(f"ダウンロード完了: {audio_file}")
            return audio_file
    except Exception as e:
        print(f"エラーが発生しました: {str(e)}")
        return None


def main():
    """メイン関数"""
    print("=" * 50)
    print("YouTube音声ダウンローダー")
    print("=" * 50)

    while True:
        url = input("\nYouTubeのURLを入力してください（終了する場合は 'q' を入力）: ").strip()

        if url.lower() == 'q':
            print("プログラムを終了します。")
            break

        if not url:
            print("URLが入力されていません。")
            continue

        # ダウンロード実行
        result = download_audio(url)

        if result:
            print(f"\n✓ 保存されました: {result}")
        else:
            print("\n✗ ダウンロードに失敗しました。")


if __name__ == "__main__":
    main()
