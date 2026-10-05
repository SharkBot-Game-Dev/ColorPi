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
          >プライバシーポリシー</h1><br/><br/>
        </div>

        <div className="bg-[var(--bg-menu)] p-5 rounded-xl m-5">
          <h3 className="m-5 text-xl">語句の解説</h3>
          <ul>
            <li>「Bot」とは、本サービスのColorPiのことを表す。</li>
            <li>「ユーザー」とは、本サービスの使用者のことを表す。</li>
          </ul>
        </div>

        <div className="bg-[var(--bg-menu)] p-5 rounded-xl m-5">
         <h3 className="m-5 text-xl">保存するデータ</h3>
          <p>本Botでは、以下のデータを保存・もしくは使用します。</p>
          <ul>
            <li>実行したコマンドのデータ</li>
            <li>Botをインストールした、サーバーとチャンネルの情報</li>
            <li>コマンド（BotのUIも含む）を実行したサーバー、チャンネルとユーザーの情報</li>
            <li>サブスクリプションなどを購入したことを示すデータ</li>
          </ul>
        </div>

        <div className="bg-[var(--bg-menu)] p-5 rounded-xl m-5">
          <h3 className="m-5 text-xl">データの収集方法・保存方法</h3>
          <p>データは、Botがそのデータを必要とする場合に収集、または保存します。<br/>
          保存場所は、MongoDBや、Redis（データベース）を用いて、本Botを運用しているサーバーに保存されます。</p>
        </div>

        <div className="bg-[var(--bg-menu)] p-5 rounded-xl m-5">
          <h3 className="m-5 text-xl">データの削除</h3>
          <p>データの削除はサポートサーバーにて問い合わせることで削除申請が可能です。</p>
        </div>

        <div className="bg-[var(--bg-menu)] p-5 rounded-xl m-5">
          <h3 className="m-5 text-xl">決済情報</h3>
          <p>また、このデータは決済情報の第三者（Stripe）への提供を行う場合があります。</p>
        </div>

        <div className="bg-[var(--bg-menu)] p-5 rounded-xl m-5">
          <h3 className="m-5 text-xl">本ポリシーの変更</h3>
          <p>運営者はBotの更新・法律の変更を反映するために、本ポリシーを変更することがあります。<br/>
いかなる変更も、運営者はユーザーに通知義務がないこととします。<br/>
本ポリシーを更新した時点で変更後のポリシーが有効となります。</p>
        </div>
      </section>
    </ center>
  );
}
