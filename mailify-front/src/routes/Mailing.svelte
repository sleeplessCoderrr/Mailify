<script lang="ts">
    import type {Request} from "../lib/interfaces/Request";
    import MailingBackground from "../components/background/MailingBackground.svelte";

    let request: Request = {
        name: "",
        receiver: "",
        emailGoals: "",
        activeCategory: ""
    }

    const categories: string[] = ["Applying Job", "College"];
    let activeCategory: string = "Applying Job";
    let activeTab: "send" | "reply" = "send";

    function setActiveCategory(category: string) {
        activeCategory = category;
    }

    function handleSubmit() {
        console.log({
            request: Request,
        });
        alert("Email content generated!");
    }
</script>

<div class="min-h-screen text-midnight font-helvetica p-6 justify-items-center items-center">
    <MailingBackground/>
    <div class="max-w-4xl mx-auto rounded-lg p-8
                bg-white/40 shadow-lg backdrop-blur">

        <div class="flex space-x-4 border-b pb-4">
            <button
                    class={`py-2 px-4 rounded ${activeTab === 'send' ? 'bg-blaze text-white' : 'bg-mist text-midnight'}`}
                    on:click={() => activeTab = 'send'}
            >
                Send Email
            </button>
            <button
                    class={`py-2 px-4 rounded ${activeTab === 'reply' ? 'bg-blaze text-white' : 'bg-mist text-midnight'}`}
                    on:click={() => activeTab = 'reply'}
            >
                Reply Email
            </button>
        </div>

        {#if activeTab === 'send'}
            <div class="mt-6">
                <label class="block text-sm font-medium">Your Name</label>
                <input
                        class="w-full mt-1 p-2 border rounded"
                        type="text"
                        placeholder="e.g., John Davis"
                        bind:value={request.name}
                />

                <label class="block mt-4 text-sm font-medium">To (Receiver)</label>
                <input
                        class="w-full mt-1 p-2 border rounded"
                        type="text"
                        placeholder="e.g., Elon Musk"
                        bind:value={request.receiver}
                />

                <label class="block mt-4 text-sm font-medium">What’s your email goal? Key points:</label>
                <textarea
                        class="w-full mt-1 p-2 border rounded h-32"
                        placeholder="Write your email goals here..."
                        bind:value={request.emailGoals}
                ></textarea>
            </div>
        {:else if activeTab === 'reply'}
            <div class="mt-6">
                <label class="block text-sm font-medium">Your Name</label>
                <input
                        class="w-full mt-1 p-2 border rounded"
                        type="text"
                        placeholder="e.g., John Davis"
                        bind:value={request.name}
                />

                <label class="block mt-4 text-sm font-medium">To (Receiver)</label>
                <input
                        class="w-full mt-1 p-2 border rounded"
                        type="text"
                        placeholder="e.g., Elon Musk"
                        bind:value={request.receiver}
                />

                <label class="block mt-4 text-sm font-medium">What’s your reply about? Key points:</label>
                <textarea
                        class="w-full mt-1 p-2 border rounded h-32"
                        placeholder="Write your reply key points here..."
                        bind:value={request.emailGoals}
                ></textarea>
            </div>
        {/if}

        <div class="flex space-x-4 mt-6">
            {#each categories as category}
                <button
                        class={`py-2 px-4 rounded ${
                        activeCategory === category
                            ? "bg-blaze text-white"
                            : "bg-mist text-midnight"
                    }`}
                        on:click={() => setActiveCategory(category)}
                >
                    {category}
                </button>
            {/each}
        </div>

        <button
                class="mt-6 w-full bg-blaze/80 text-white py-2 rounded hover:bg-blaze ease-in-out duration-300"
                on:click={handleSubmit}
        >
            Generate Email
        </button>
    </div>
</div>

<style>
    h2 {
        cursor: pointer;
    }
</style>
