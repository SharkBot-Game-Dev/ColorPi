import './App.css'
import { useEffect, useState } from 'react'
import type { DiscordUser, DiscordUserGuilds } from './type/discord';

function App() {
  const [discordUser, setDiscordUser] = useState<DiscordUser | undefined>(undefined);
  const [discordUserGuilds, setDiscordUserGuilds] = useState<DiscordUserGuilds[] | undefined>(undefined);

  useEffect(() => {
    fetch("/api/user_info")
      .then((res) => {
        if (res.status == 401) {
            return {"status": "error"}
        } else {
            return res.json();
        }
      })
      .then((data) => {
        if (data.status == "error") {
            setDiscordUser(undefined);
        } else {
            setDiscordUser(data)
        }
      });

    fetch("/api/guilds")
      .then((res) => {
        if (res.status == 401) {
            return {"status": "error"}
        } else {
            return res.json();
        }
      })
      .then((data) => {
        if (data.status == "error") {
            setDiscordUserGuilds(undefined);
        } else {
            setDiscordUserGuilds(data.filter((guild: DiscordUserGuilds) => guild.owner))
        }
      });
  }, []);

  return (
    <>
      <section id="center">
        <div>
          <h1>{discordUser ? `${discordUser.username}さん、よろしく！` : "ログインが必要です。"}</h1>
          <p>
            {discordUser ? "サーバーを選択してください。" : "以下のボタンからログインしてください。"}
          </p><br/>
        </div>

        {discordUserGuilds ? <div>
            {discordUserGuilds.map((value) => <div className='serverBox'>
                <h5>{value.name}</h5>
            </div>)}
        </div> : <div className='inviteButton'>
          <a href='/api/login'>ログインする</a><br/><br/>
        </div>}
      </section>
    </>
  )
}

export default App
