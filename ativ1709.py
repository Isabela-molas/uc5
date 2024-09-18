import sys #para funções relacionadas ao sistema
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout  #para widgets GUI 
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput #para funcionalidade multimídia
from PySide6.QtCore import QUrl  #para funcionalidade principal

class MusicPlayer(QWidget):
    def __init__(self):
        super().__init__()

        # Configuração da janela
        self.setWindowTitle("Spotify")
        self.setGeometry(300, 300, 300, 100)

      
        self.layout = QVBoxLayout()
        self.play_button = QPushButton("Play", self)
        self.layout.addWidget(self.play_button)
        self.setLayout(self.layout)

       
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        
        music_file_path = "/path/to/your/music/file.mp3"
        self.player.setSource(QUrl.fromLocalFile(music_file_path))

        
        self.play_button.clicked.connect(self.toggle_music)

   
        self.is_playing = False

    def toggle_music(self):
        if self.is_playing:
            self.player.pause()
            self.play_button.setText("Play")
        else:
            self.player.play()
            self.play_button.setText("Pause")

       
        self.is_playing = not self.is_playing


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MusicPlayer()
    window.show()
    sys.exit(app.exec())
