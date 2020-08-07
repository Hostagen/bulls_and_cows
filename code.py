import random #random 모듈 import 해줘야 난수 생성 가능함

@bot.command(name="야구")
async def bulls_and_cows(ctx):
    random_nums=["0", "0", "0"]
    random_nums[0]=str(random.randrange(1, 9, 1))
    random_nums[1]=random_nums[0]
    random_nums[2]=random_nums[0]

    while (random_nums == random_nums[1]):
        random_nums[1]=str(random.randrange(1, 9, 1))
    while (random_nums[0] == random_nums[2] or random_nums[1] == random_nums[2]):
        random_nums[2] = str(random.randrange(1, 9, 1))

    try_count=0
    strike_count=0
    ball_count=0

    embed=discord.Embed(title="숫자 3자리를 입력해주세요.")
    embed.set_footer(text="그만하시고 싶으시면 'stop'이라고 입력해주세요.")
    plz_input_nums=await ctx.send(embed=embed)
    print(random_nums)
    while (strike_count < 3):
        def check(m):
            return m.author == ctx.author

        msg=await bot.wait_for('message', check=check)

        if msg.content == "stop":
            await plz_input_nums.delete()
            return

        if msg.content.isdigit() is False:
            embed=discord.Embed(title="숫자만 입력해주세요.")
            embed.set_footer(text="다시 입력해주세요.")
            await plz_input_nums.edit(embed=embed)
            continue

        if len(msg.content) > 3:
            embed=discord.Embed(title="입력된 숫자가 너무 많습니다!", description="3자리만 입력해주세요.")
            embed.set_footer(text="다시 입력해주세요.")
            await plz_input_nums.edit(embed=embed)
            continue
        elif len(msg.content) < 3:
            embed=discord.Embed(title="입력된 숫자가 너무 적습니다!", description="3자리만 입력해주세요.")
            embed.set_footer(text="다시 입력해주세요.")
            await plz_input_nums.edit(embed=embed)
            continue

        strike_count=0
        ball_count=0
        
        for i in range(0, 3):
            for j in range(0, 3):
                if(msg.content[i] == str(random_nums[j]) and i == j):
                    strike_count += 1
                elif(msg.content[i] == str(random_nums[j]) and i != j):
                    ball_count += 1

        embed=discord.Embed(title=f"입력한 숫자: {msg.content}", description=f"[ {strike_count} ]번의 스트라이크 [ {ball_count} ]개의 볼")
        embed.set_footer(text="계속해서 숫자를 입력해주세요.")
        await plz_input_nums.edit(embed=embed)
        try:
            await msg.delete()
        except:
            pass
        try_count += 1

    embed=discord.Embed(title=f"{try_count}번 만에 정답을 맞추셨습니다.", description=ctx.message.author.mention)
    await plz_input_nums.edit(embed=embed)
