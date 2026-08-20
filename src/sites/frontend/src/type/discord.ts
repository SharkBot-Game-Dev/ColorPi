export type DiscordUser = {
  username: string;
  id: string;
  avatar: string | null;
};

export type DiscordUserGuilds = {
  id: string;
  name: string;
  icon: string | null;
  owner: boolean;
};