import yt_dlp
import os


def download_video(url, output_path='downloads', quality='best', download_subtitles=False):
    """
    YouTubeのURLから動画をダウンロードする

    Args:
        url (str): YouTubeの動画URL
        output_path (str): 保存先ディレクトリ（デフォルト: 'downloads'）
        quality (str): 動画品質（'best', 'high', 'medium', 'low'）
        download_subtitles (bool): 字幕をダウンロードするかどうか（デフォルト: False）
    """
    # 保存先ディレクトリが存在しない場合は作成
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # 品質設定
    quality_formats = {
        'best': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'high': 'bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[height<=1080][ext=mp4]',
        'medium': 'bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/best[height<=720][ext=mp4]',
        'low': 'bestvideo[height<=480][ext=mp4]+bestaudio[ext=m4a]/best[height<=480][ext=mp4]',
    }

    # yt-dlpのオプション設定
    ydl_opts = {
        'format': quality_formats.get(quality, quality_formats['best']),
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),  # 出力ファイル名
        'merge_output_format': 'mp4',  # 出力形式をMP4に統一
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

    # 字幕ダウンロード設定
    if download_subtitles:
        ydl_opts['writesubtitles'] = True  # 字幕をダウンロード
        ydl_opts['writeautomaticsub'] = True  # 自動生成字幕もダウンロード
        ydl_opts['subtitleslangs'] = ['ja', 'en']  # 日本語と英語の字幕
        ydl_opts['subtitlesformat'] = 'srt'  # SRT形式で保存

    try:
        print(f"ダウンロード開始: {url}")
        print(f"品質設定: {quality}")
        if download_subtitles:
            print("字幕ダウンロード: 有効")

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # 動画情報を取得
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            print(f"ダウンロード完了: {filename}")

            # 字幕ファイルの確認
            if download_subtitles:
                base_filename = os.path.splitext(filename)[0]
                subtitle_files = []
                for lang in ['ja', 'en']:
                    subtitle_file = f"{base_filename}.{lang}.srt"
                    if os.path.exists(subtitle_file):
                        subtitle_files.append(subtitle_file)
                        print(f"字幕ファイル: {subtitle_file}")

                if subtitle_files:
                    print(f"✓ {len(subtitle_files)}個の字幕ファイルをダウンロードしました")
                else:
                    print("字幕ファイルが見つかりませんでした（この動画には字幕がない可能性があります）")

            return filename
    except Exception as e:
        print(f"エラーが発生しました: {str(e)}")
        return None


def main():
    """メイン関数"""
    print("=" * 50)
    print("YouTube動画ダウンローダー")
    print("=" * 50)

    while True:
        url = input("\nYouTubeのURLを入力してください（終了する場合は 'q' を入力）: ").strip()

        if url.lower() == 'q':
            print("プログラムを終了します。")
            break

        if not url:
            print("URLが入力されていません。")
            continue

        # 品質選択
        print("\n品質を選択してください:")
        print("1. 最高品質 (best)")
        print("2. 高品質 - 1080p (high)")
        print("3. 中品質 - 720p (medium)")
        print("4. 低品質 - 480p (low)")

        choice = input("選択 (1-4, デフォルトは1): ").strip()

        quality_map = {
            '1': 'best',
            '2': 'high',
            '3': 'medium',
            '4': 'low',
            '': 'best'  # デフォルト
        }

        quality = quality_map.get(choice, 'best')

        # 字幕ダウンロードの確認
        print("\n字幕もダウンロードしますか?")
        subtitle_choice = input("はい (y) / いいえ (n, デフォルトはいいえ): ").strip().lower()
        download_subtitles = subtitle_choice in ['y', 'yes', 'はい', 'ハイ']

        # ダウンロード実行
        result = download_video(url, quality=quality, download_subtitles=download_subtitles)

        if result:
            print(f"\n✓ 保存されました: {result}")
        else:
            print("\n✗ ダウンロードに失敗しました。")


if __name__ == "__main__":
    main()
