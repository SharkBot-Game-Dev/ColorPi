import Image from "next/image";

export default function Home() {
  return (
    <center
      id="root"
      className="
        relative
        mx-auto
        flex
        min-h-[100svh]
        w-[1126px]
        max-w-full
        flex-col
        box-border
        text-center
      "
    >
      <section id="center" className="text-center">
        <div>
          <Image src="/avatar.png" width={100} height={100} alt="avatar" className="size-[100px] inline-block" />

          <h1
            className="
              my-8
              text-[56px]
              font-medium
              tracking-[-1.68px]
              text-[var(--text-h)]
              max-lg:my-5
              max-lg:text-4xl
            "
          >ColorPi🎨</h1>
          <p>
            初心者におすすめの多機能Bot
          </p><br/><br/>
        </div>

        <a
          href="#"
          className="
            rounded-[50px]
            bg-[var(--button-bg)]
            p-5
            text-[var(--button-text)]
            no-underline
          "
        >
          招待する
        </a>
        <br/><br/>

        <div className="bg-[var(--bg-menu)] p-5 rounded-xl m-5">
          <h3 className="m-5 text-xl">便利なコマンド😽</h3>
          <p>サーバーを便利にする楽しいコマンドがいっぱい！</p>
          <ul>
            <li>/user 😺ユーザー情報を表示できる</li>
            <li>/avatar 😆好きな人のアバターを表示</li>
            <li>/clear 🧹スパムメッセージを一気に削除</li>
          </ul>
        </div>

        <div className="bg-[var(--bg-menu)] p-5 rounded-xl m-5">
         <h3 className="m-5 text-xl">ロールパネル😆</h3>
          <p>ロールをつけたり外したりできる機能があるよ！</p>
          <ul>
            <li>/panel 😆ロールパネルを作成</li>
            <li>/guideline ✅ルールに同意できるパネルが作れる</li>
          </ul>
        </div>

        <div className="bg-[var(--bg-menu)] p-5 rounded-xl m-5">
          <h3 className="m-5 text-xl">いろんな色コマンド🎨</h3>
          <p>色を表示したり、かわいいBotのアバターを作成したり..！</p>
          <ul>
            <li>/draw 🎨Botのアバター風画像を作成</li>
            <li>/color 🖌️色を表示できる</li>
          </ul>
        </div>

        <div className="bg-[var(--bg-menu)] p-5 rounded-xl m-5">
          <h3 className="m-5 text-xl">機能はほとんどが無料！💰</h3>
          <p>ほとんどの機能が無料で使用できます。</p>
        </div>

        <div className="p-5 m-5">
          <h3 className="m-5 text-xl">さあ、今すぐサーバーをアップグレードしよう！👇</h3><br/>
          <a
            className="
              rounded-[50px]
              bg-[var(--button-bg)]
              p-5
              text-[var(--button-text)]
              no-underline
            " 
            href='https://discord.com/oauth2/authorize?client_id=1537996178157871154'
          >今すぐ招待する</a>
        </div>
      </section>
    </ center>
  );
}
