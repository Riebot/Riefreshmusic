import os
from MightyMusic.config import ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,OWNER_USERNAME
class Messages():
      START_MSG = "**Hayyy 👋** [{}](tg://user?id={}) \n━━━━━━━━━━━━━━━━━━━━━━━━\n🎙 Saya adalah bot musik yang di kelola oleh @(OWNER_USERNAME) untuk memutar musik di obrolan suara Grup & Saluran Channel Telegram.\n\n📝 Ketik /help di bawah untuk mendapatkan info dari saya.\n━━━━━━━━━━━━━━━━━━━━━━━━\n📻 Selamat menikmati dan mendengarkan musik di Voice call GROUP/ CHANNEL kamu."
      HELP_MSG = [
        ".",
f"""
**Hay kamu, bertemu lagi dengan saya {PROJECT_NAME}

📍 {PROJECT_NAME} bisa memutar musik di Voice call Group atau Voice call Channel, Slipkol juga bisa kok bhakss 😆

📼 Assistant bot >> @{ASSISTANT_NAME}\n\nKlik tombol dibawah untuk melihat intruksi lain**
📣 Channel >> @infobotmusik
☕ Created >> [Ari](https://t.me/SilenceSpe4ks)
""",

f"""
**↘ Pengaturan Utama ↙**

1) Membuat bot admin (Group dan di channel jika menggunakan cplay)
2) Mulai obrolan suara
3) Coba /play [nama lagu] pertama kali oleh admin
*) Jika userbot bergabung nikmati musik, Jika tidak tambahkan @{ASSISTANT_NAME} ke grup Anda dan coba lagi

**↘ Untuk Channel Music Play ↙**
1) Jadikan saya admin saluran Anda
2) Kirim /userbotjoinchannel di grup tertaut
3) Sekarang kirim perintah di grup tertaut

**🔛 Beberapa Command 📍**

**⏺ Cara Memainkan Lagu ⏸**

• /play <nama lagu> : putar lagu yang Anda minta
• /play <url youtube> : Putar lagu melalui balasan url youtube
• /play <balas ke audio> : putar file balasan
• /dplay <nama lagu> : putar lagu yang Anda minta melalui deezer
• /splay <nama lagu> : putar lagu yang Anda minta melalui jio saavn

**🔁 Playback ⏩**

• /player: buka panel pengaturan pemutar musik
• /skip: putar lagu berikutnya
• /pause: jeda pemutaran lagu
• /resume: melanjutkan pemutaran lagu
• /end: hentikan pemutaran musik
• /current: Tampilkan sedang diputar
• /playlist: Tampilkan daftar yang sedang diputar

*Cmd player dan semua cmd lain kecuali /play, /current dan /playlist hanya untuk admin grup*
""",
        
f"""
**⏸Putar Musik Di Channel 📢**

🔔 Hanya untuk admin grup tertaut:

• /cplay [song name] - putar lagu yang Anda minta
• /cdplay [song name] - putar lagu yang Anda minta via deezer
• /csplay [song name] - putar lagu yang Anda minta via jio saavn
• /cplaylist - Perlihatkan daftar yang dimainkan
• /cccurrent - Perlihatkan yang diputar sekarang
• /cplayer - buka panel pengaturan pemutar musik
• /cpause - jeda pemutaran lagu
• /cresume - lanjutkan pemutaran lagu
• /cskip - putar lagu berikutnya
• /cend - stop pemutaran lagu
• /userbotjoinchannel - Undang asisten ke chat kamu

saluran Channel juga dapat digunakan sebagai pengganti c ( /cplay = /channelplay )

🔔 Jika Anda tidak suka bermain di grup tertaut:

1) Dapatkan ID saluran Anda.
2) Buat grup dengan judul: Channel Music: your_channel_id
3) Tambahkan bot sebagai admin Saluran dengan izin penuh
4) Tambahkan @{ASSISTANT_NAME} ke saluran sebagai admin.
5) Cukup kirim perintah di grup Anda.
""",

f"""
**🗒 More Info 📲**

• /admincache: Memperbarui info admin grup Anda. Coba jika bot tidak mengenali admin
• /userbotjoin: Undang @{ASSISTANT_NAME} Userbot ke obrolan Anda

**📣 Command Khusus buat pengguna sudo**

 • /userbotleaveall - Keluarkan asisten musik dari semua obrolan chat
 • /gcast <reply to message> - global brodcast membalas pesan ke semua obrolan
 • /pmpermit [on/off] - enable/disable pesan pmpermit 
*Pengguna Sudo dapat menjalankan perintah apa pun di grup mana pun

☕ Owner Project: [arie](https://t.me/SilenceSpe4ks)

"""
      ]
