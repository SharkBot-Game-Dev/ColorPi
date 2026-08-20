import avatarLogo from './assets/avatar.png'
import './App.css'

function App() {
  return (
    <>
      <section id="center">
        <div>
          <img src={avatarLogo} width={100} height={100} />

          <h1>ColorPi🎨</h1>
          <p>
            初心者におすすめの多機能Bot
          </p><br/>
        </div>

        <div className='inviteButton'>
          <a href='https://discord.com/oauth2/authorize?client_id=1537996178157871154'>Discordに追加</a>
        </div><br/><br/>

        <div>
          <h3>便利なコマンド😽</h3>
          <p>サーバーを便利にする楽しいコマンドがいっぱい！</p>
          <ul>
            <li>/user 😺ユーザー情報を表示できる</li>
            <li>/avatar 😆好きな人のアバターを表示</li>
            <li>/clear 🧹スパムメッセージを一気に削除</li>
          </ul>
        </div>

        <div>
          <h3>ロールパネル😆</h3>
          <p>ロールをつけたり外したりできる機能があるよ！</p>
          <ul>
            <li>/panel 😆ロールパネルを作成</li>
            <li>/guideline ✅ルールに同意できるパネルが作れる</li>
          </ul>
        </div>

        <div>
          <h3>いろんな色コマンド🎨</h3>
          <p>色を表示したり、かわいいBotのアバターを作成したり..！</p>
          <ul>
            <li>/draw 🎨Botのアバター風画像を作成</li>
            <li>/color 🖌️色を表示できる</li>
          </ul>
        </div>

        <div>
          <h3>機能はほとんどが無料！💰</h3>
          <p>ほとんどの機能が無料で使用できます。</p>
        </div>

        <div className='inviteButton'>
          <h3>さあ、今すぐサーバーをアップグレードしよう！👇</h3><br/><br/>
          <a href='https://discord.com/oauth2/authorize?client_id=1537996178157871154'>今すぐ招待する</a>
        </div><br/><br/>
      </section>
    </>
  )
}

export default App
