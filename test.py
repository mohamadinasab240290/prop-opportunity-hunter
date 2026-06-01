# ---------------- PROP BONUSES & COMPETITIONS ----------------
def get_prop_opportunities():
    opportunities = []
    # 🏆 Free competitions (sample + real-world style)
    competitions = [
        "🏆 Demo Trading Contest - TabTrade x BestPropFirms (Free Entry, Prize Pool $13,000)",
        "🏆 Prop Challenge Leaderboard Contest - Top 50 get funded vouchers",
        "🏆 Monthly Free Evaluation Challenges (various prop firms)"
    ]
    # 🎁 Bonuses & promos
    bonuses = [
        "🎁 The5ers - Discount + Free Account after payout (promo active)",
        "🎁 BrightFunded - 15% OFF + reward account after challenge",
        "🎁 Blue Guardian - 35% OFF + refund rewards",
        "🎁 Funding Pips - periodic discount codes + promos",
        "🎁 FX brokers - occasional No Deposit Bonus offers (region dependent)"
    ]
    # 💼 Free funded opportunities
    funded = [
        "💼 Some prop firms offer FREE trial funded accounts (limited seats)",
        "💼 Affiliate programs with free starter accounts ($1000 - $10k)",
        "💼 Demo-to-funded conversion competitions"
    ]
    opportunities.extend(competitions)
    opportunities.extend(bonuses)
    opportunities.extend(funded)
    return opportunities
prop_opps = get_prop_opportunities()
# ---------------- ADD TO MESSAGE ----------------
message += "\n\n💼 PROP OPPORTUNITIES\n"
for opp in prop_opps:
    message += f"{opp}\n"