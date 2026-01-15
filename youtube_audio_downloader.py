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
