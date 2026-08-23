import { getLoginUser } from "@/lib/discord/fetch";
import { cookies } from "next/headers";
import Image from "next/image";

export default async function Dashboard() {
  const cookieStore = await cookies();
  const sessionId = cookieStore.get("session_id")?.value;

  let user;
  if (sessionId) {
    try {
        user = (await getLoginUser(sessionId) as any).data;
    } catch {}
  } else {
    return <p>ログインが必要です。</p>
  }
  if (!user) {
    return <p>ログインが必要です。</p>
  }
  
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
          <img src={user?.image_url ? user?.image_url : "https://cdn.discordapp.com/embed/avatars/0.png"} width={100} height={100} alt="avatar" className="size-[100px] inline-block rounded-xl" />

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
          >{user.global_name}</h1>
          <p>
            ※ダッシュボードはβ版です。
          </p><br/><br/>
        </div>
      </section>
    </ center>
  );
}
