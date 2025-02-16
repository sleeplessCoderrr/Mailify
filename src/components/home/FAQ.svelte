<script lang="ts">
    import { faqs } from "../../lib/interfaces/FAQ";

    let openIndex = -1;
    function toggleAnswer(index:number) { openIndex = openIndex === index ? -1 : index; }
</script>

<div class="w-4/6 mx-auto mt-36 mb-24">
    <h2 class="text-4xl font-bold mb-8 text-center text-midnight">Frequently Asked Questions</h2>
    <div class="space-y-4">
        {#each faqs as faq, index}
            <div class="bg-mist/40 backdrop-blur-sm shadow-lg border-2 border-stone-300 rounded-md overflow-hidden">
                <button
                    on:click={() => toggleAnswer(index)}
                    class="flex justify-between items-center w-full p-4 text-left hover:bg-stone-200 transition-colors duration-600">
                    <span class="text-lg font-semibold text-midnight hover:bg-stone-200">{faq.question}</span>
                    <svg
                    class="w-6 h-6 text-midnight transform transition-transform duration-600 {openIndex === index ? 'rotate-180' : ''}"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                    </svg>
                </button>
                {#if openIndex === index}
                    <div class="p-4 text-midnight animate-fadeIn">
                        {faq.answer}
                    </div>
                {/if}
            </div>
        {/each}
    </div>
</div>

<style>
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    .animate-fadeIn {
        animation: fadeIn 0.6s ease-out;
    }
</style>