# roast_engine.py

import re


def generate_roast(text):
    roasts = []

    text_lower = text.lower()
    words = text.split()

    word_count = len(words)

    # ---------------------------------------------------
    # Resume Length
    # ---------------------------------------------------

    if word_count < 180:
        roasts.append({
            "title": "Tiny Resume Energy",
            "message": (
                "This resume is so short that recruiters may think "
                "the second page failed to load. You need stronger project "
                "descriptions, measurable impact, and actual detail."
            )
        })

    elif word_count > 900:
        roasts.append({
            "title": "Autobiography Detected",
            "message": (
                "Your resume is approaching documentary length. "
                "Recruiters spend seconds scanning resumes, not hours "
                "reviewing your life's cinematic universe."
            )
        })

    # ---------------------------------------------------
    # Buzzword Detection
    # ---------------------------------------------------

    buzzwords = [
        "hardworking",
        "passionate",
        "motivated",
        "dynamic",
        "team player",
        "innovative",
        "enthusiastic",
        "dedicated"
    ]

    found_buzzwords = [w for w in buzzwords if w in text_lower]

    if found_buzzwords:
        roasts.append({
            "title": "LinkedIn Influencer Vocabulary",
            "message": (
                f"You used these buzzwords: "
                f"{', '.join(found_buzzwords)}. "
                "Every resume on Earth says this. "
                "Replace personality adjectives with proof of work."
            )
        })

    # ---------------------------------------------------
    # Metrics Check
    # ---------------------------------------------------

    achievement_words = [
        "improved",
        "increased",
        "optimized",
        "reduced",
        "developed",
        "built"
    ]

    has_achievement_words = any(
        word in text_lower for word in achievement_words
    )

    has_metrics = bool(re.search(r"\d+%|\d+x|\$\d+", text))

    if has_achievement_words and not has_metrics:
        roasts.append({
            "title": "Trust Me Bro Metrics",
            "message": (
                "You claim you improved and optimized things, "
                "but provided zero measurable impact. "
                "Numbers make achievements believable. "
                "Without metrics, it sounds fictional."
            )
        })

    # ---------------------------------------------------
    # Skills Overload
    # ---------------------------------------------------

    skill_keywords = [
        "python", "java", "c++", "sql", "excel",
        "machine learning", "docker", "aws",
        "power bi", "tableau"
    ]

    skill_count = sum(
        text_lower.count(skill)
        for skill in skill_keywords
    )

    if skill_count > 20:
        roasts.append({
            "title": "Skill Section Inflation",
            "message": (
                "Your skills section looks like you swallowed "
                "an entire Udemy catalog. Recruiters prefer depth "
                "over keyword spam."
            )
        })

    # ---------------------------------------------------
    # Project Quality
    # ---------------------------------------------------

    project_count = text_lower.count("project")

    if project_count <= 1:
        roasts.append({
            "title": "Project Drought",
            "message": (
                "One project is not enough in today's market. "
                "Right now your resume gives 'watched tutorials' "
                "instead of 'built things'."
            )
        })

    # ---------------------------------------------------
    # GitHub Mention
    # ---------------------------------------------------

    if "github" not in text_lower:
        roasts.append({
            "title": "No GitHub Found",
            "message": (
                "You are applying to technical roles without "
                "showing a GitHub profile. Recruiters now expect "
                "proof that your projects actually exist."
            )
        })

    # ---------------------------------------------------
    # Experience Check
    # ---------------------------------------------------

    experience_words = [
        "intern",
        "experience",
        "worked",
        "developer",
        "engineer"
    ]

    if not any(word in text_lower for word in experience_words):
        roasts.append({
            "title": "Experience Section Missing",
            "message": (
                "This resume feels academically manufactured. "
                "Even small internships, freelancing, volunteering, "
                "or collaborative projects help establish credibility."
            )
        })

    # ---------------------------------------------------
    # Email Check
    # ---------------------------------------------------

    funny_email_patterns = [
        "cool",
        "killer",
        "pro",
        "gamer",
        "legend"
    ]

    if any(word in text_lower for word in funny_email_patterns):
        roasts.append({
            "title": "Questionable Email Choices",
            "message": (
                "Your email sounds like it was created during "
                "a middle-school gaming phase. Professionalism matters."
            )
        })

    # ---------------------------------------------------
    # Default Roast
    # ---------------------------------------------------

    if not roasts:
        roasts.append({
            "title": "Unexpectedly Competent",
            "message": (
                "This resume is suspiciously solid. "
                "Clear structure, reasonable detail, and decent balance. "
                "Either you actually know what you're doing "
                "or you copied from someone very experienced."
            )
        })

    return roasts