import os
from PyPDF2 import PdfFileMerger

# 同じディレクトリ内のPDFファイルのリストを取得
pdf_files = [file for file in os.listdir() if file.endswith('.pdf')]

# PDFファイルが存在しない場合のエラーチェック
if not pdf_files:
    print("ディレクトリ内にPDFファイルが見つかりません。")
else:
    # PDFファイルを結合するためのPdfFileMergerオブジェクトを作成
    pdf_merger = PdfFileMerger()

    # 各PDFファイルを結合
    for pdf_file in pdf_files:
        pdf_merger.append(pdf_file)

    # 結合したPDFを新しいファイルに保存
    merged_pdf_name = 'merged.pdf'
    pdf_merger.write(merged_pdf_name)

    # 終了時に必ずファイルをクローズ
    pdf_merger.close()

    print(f"{len(pdf_files)} つのPDFファイルを {merged_pdf_name} に結合しました。")
