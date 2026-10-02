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
            私たちは、様々な製品を作っています。
          </p><br/>

          <br/>

          <h2 className="text-[26px] font-medium">製品とサービス</h2><br/>
          <div className="m-5">
            <div className="p-1 bg-[var(--bg-menu)] text-center rounded-lg p-5">
              <a href="/products/bot">
                <h3>多機能Bot (ColorPi)</h3>
                <p className="text-white">
                  初心者におすすめの多機能Botです。<br/><br/>
                  👉️ 移動するにはクリック 👈️
                </p>
              </a>
            </div>
          </div>
        </div>
      </section>
    </ center>
  );
}
