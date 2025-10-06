import asyncio
from crawl4ai import (
    AsyncWebCrawler,
    CacheMode,
    CrawlerRunConfig,
    DefaultMarkdownGenerator,
)
from crawl4ai.deep_crawling import BFSDeepCrawlStrategy
from crawl4ai.content_filter_strategy import PruningContentFilter
from crawl4ai.content_scraping_strategy import (
    LXMLWebScrapingStrategy,
)
from crawl4ai.deep_crawling.filters import (
    FilterChain,
    URLPatternFilter,
    DomainFilter,
)


async def main():
    filter_chain = FilterChain(
        [
            URLPatternFilter(patterns=["*docs*"]),
            DomainFilter(
                allowed_domains=["sst.dev"],
                blocked_domains=[
                    "movies.sst.dev",
                    "discourse.sst.dev",
                    "console.sst.dev",
                ],  # Only allow sst.dev domain
            ),
        ]
    )
    config = CrawlerRunConfig(
        cache_mode=CacheMode.ENABLED,
        # Tag exclusions
        excluded_tags=["form", "header", "footer", "nav"],
        # Link filtering
        exclude_external_links=True,
        exclude_social_media_links=True,
        markdown_generator=DefaultMarkdownGenerator(
            content_filter=PruningContentFilter(
                threshold=0.48, threshold_type="fixed", min_word_threshold=0
            )
        ),
        deep_crawl_strategy=BFSDeepCrawlStrategy(
            max_depth=10, filter_chain=filter_chain, include_external=False
        ),
        scraping_strategy=LXMLWebScrapingStrategy(),
        verbose=True,
    )

    async with AsyncWebCrawler() as crawler:
        results = await crawler.arun("https://sst.dev/docs/", config=config)
        file_content = ""
        print(f"Crawled {len(results)} pages in total")

        # Access individual results
        for result in results:
            file_content += result.markdown.raw_markdown + "\n\n"

        with open("sstv3.md", "w") as file:
            file.write(file_content)


if __name__ == "__main__":
    asyncio.run(main())
