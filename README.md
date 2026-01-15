# YouTube ダウンローダー

yt-dlp を使用した YouTube 動画および音声ダウンローダーです。  
このツールは、YouTube の動画を MP4 形式でダウンロードしたり、音声を MP3 形式で抽出してダウンロードしたりすることができます。

## 機能

- **動画ダウンローダー** (`youtube_video_downloader.py`): YouTube の動画を様々な品質でダウンロード
- **音声ダウンローダー** (`youtube_audio_downloader.py`): YouTube の動画から音声のみを MP3 形式で抽出・ダウンロード

## 必要条件

- Python 3.6 以上
- yt-dlp
- FFmpeg (音声抽出に必要)

## インストール

1. リポジトリをクローンまたはダウンロードしてください。

2. 依存関係をインストールします：
   ```
   pip install -r requirements.txt
   ```

3. FFmpeg をインストールしてください：
   - Windows: [FFmpeg 公式サイト](https://ffmpeg.org/download.html) からダウンロード
   - macOS: `brew install ffmpeg`
   - Linux: `sudo apt install ffmpeg` (Ubuntu/Debian)

## 使い方

### 動画ダウンローダー

`youtube_video_downloader.py` を実行します：

```bash
python youtube_video_downloader.py
```

プログラムが起動したら、YouTube の URL を入力し、品質を選択してください。  
ダウンロードされたファイルは `downloads/` フォルダに保存されます。

品質オプション：
- 最高品質 (best)
- 高品質 - 1080p (high)
- 中品質 - 720p (medium)
- 低品質 - 480p (low)

### 音声ダウンローダー

`youtube_audio_downloader.py` を実行します：

```bash
python youtube_audio_downloader.py
```

プログラムが起動したら、YouTube の URL を入力してください。  
音声が MP3 形式で `downloads/` フォルダに保存されます。

## 注意事項

- このツールは個人使用を目的としています。著作権のあるコンテンツのダウンロードは法的責任を負う可能性があります。
- YouTube の利用規約を確認し、遵守してください。
- ダウンロードしたコンテンツの使用は自己責任でお願いします。

## ライセンス

このプロジェクトは MIT ライセンスの下で公開されています。