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
          >利用規約</h1><br/><br/>
        </div>

        <div className="bg-[var(--bg-menu)] p-5 rounded-xl m-5">
          <h3 className="m-5 text-xl">語句の解説</h3>
          <ul>
            <li>「Bot」とは、本サービスのColorPiのことを表す。</li>
            <li>「ユーザー」とは、本サービスの使用者のことを表す。</li>
          </ul>
        </div>

        <div className="bg-[var(--bg-menu)] p-5 rounded-xl m-5">
         <h3 className="m-5 text-xl">使用者は以下の行為をしないものとする</h3>
          <p>本Botでは、以下のデータを保存・もしくは使用します。</p>
          <ul>
            <li>犯罪行為に関連する行為</li>
            <li>サーバーまたはネットワークの機能を破壊したり、妨害したりする行為</li>
            <li>Botに攻撃をすること。</li>
            <li>運営を妨害するおそれのある行為</li>
            <li>他のユーザーに関する個人情報等を収集または蓄積する行為</li>
            <li>コマンドを悪用する行為</li>
            <li>Botの機能を悪用する行為</li>
          </ul>
        </div>

        <div className="bg-[var(--bg-menu)] p-5 rounded-xl m-5">
          <h3 className="m-5 text-xl">以下に当てはまる使用者は使用してはならないものとする。</h3>
          <ul>
            <li>荒らしに関与している使用者である場合</li>
            <li>当運営が利用することを相当でないと判断した場合</li>
            <li>Botの機能を悪用する目的である場合</li>
          </ul>
        </div>

        <div className="bg-[var(--bg-menu)] p-5 rounded-xl m-5">
          <h3 className="m-5 text-xl">運営は以下の理由の場合、サービスを一時的、<br/>または永久的に停止してよいものとする。<br/>また、責任は取らないものとする。</h3>
          <ul>
            <li>地震、落雷、火災、停電または天災などの不可抗力により、本サービスの提供が困難となった場合</li>
            <li>コンピュータシステムの保守点検または更新を行う上でやむを得ないとき</li>
            <li>電気通信事業者の都合により本サービス用通信回線の使用が不能なとき</li>
            <li>オーナーの資金が尽きたとき。</li>
            <li>データベースが壊れた場合。</li>
          </ul>
        </div>

        <div className="bg-[var(--bg-menu)] p-5 rounded-xl m-5">
          <h3 className="m-5 text-xl">利用規約の変更</h3>
          <p>運営はユーザーの許可なしに利用規約を変更できるものとする。<br/>本規約の解釈にあたっては、日本法を準拠法とする。<br/>運営の故意や重大な過失でない場合、責任は負わない。</p>
        </div>

        <div className="bg-[var(--bg-menu)] p-5 rounded-xl m-5">
          <p>以上のことに同意できない場合は、<br/>
サービスを使用できないものとする。また、サービスを使用したら、<br/>
この利用規約を読んでいなくてもこの利用規約に同意したこととなる。</p>
        </div>
      </section>
    </ center>
  );
}
