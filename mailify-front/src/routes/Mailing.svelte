<script lang="ts">
    import { onMount } from "svelte";

    let name = "";
    let receiver = "";
    let emailGoals = "";

    const categories: string[] = ["Outreach", "Walmart Discount", "Cancel Netflix", "Business"];
    let activeCategory: string = "Outreach";

    let activeTab: "send" | "reply" = "send"; // Track active tab

    function setActiveCategory(category: string) {
        activeCategory = category;
    }

    function handleSubmit() {
        console.log({
            name,
            receiver,
            emailGoals,
            activeCategory,
            activeTab
        });
        alert("Email content generated!");
    }
</script>

<!-- Page Container -->
<div class="min-h-screen bg-gray-50 text-gray-900 p-6">
    <div class="max-w-4xl mx-auto bg-white rounded-lg shadow-md p-8">

        <!-- Tab Navigation -->
        <div class="flex space-x-4 border-b pb-4">
            <button
                    class={`py-2 px-4 rounded ${activeTab === 'send' ? 'bg-purple-600 text-white' : 'bg-gray-200 text-gray-600'}`}
                    on:click={() => activeTab = 'send'}
            >
                Send Email
            </button>
            <button
                    class={`py-2 px-4 rounded ${activeTab === 'reply' ? 'bg-purple-600 text-white' : 'bg-gray-200 text-gray-600'}`}
                    on:click={() => activeTab = 'reply'}
            >
                Reply Email
            </button>
        </div>

        <!-- Content based on active tab -->
        {#if activeTab === 'send'}
            <!-- Send Email Form -->
            <div class="mt-6">
                <label class="block text-sm font-medium">Your Name</label>
                <input
                        class="w-full mt-1 p-2 border rounded"
                        type="text"
                        placeholder="e.g., John Davis"
                        bind:value={name}
                />

                <label class="block mt-4 text-sm font-medium">To (Receiver)</label>
                <input
                        class="w-full mt-1 p-2 border rounded"
                        type="text"
                        placeholder="e.g., Elon Musk"
                        bind:value={receiver}
                />

                <label class="block mt-4 text-sm font-medium">What’s your email goal? Key points:</label>
                <textarea
                        class="w-full mt-1 p-2 border rounded h-32"
                        placeholder="Write your email goals here..."
                        bind:value={emailGoals}
                ></textarea>
            </div>
        {:else if activeTab === 'reply'}
            <!-- Reply Email Form -->
            <div class="mt-6">
                <label class="block text-sm font-medium">Your Name</label>
                <input
                        class="w-full mt-1 p-2 border rounded"
                        type="text"
                        placeholder="e.g., John Davis"
                        bind:value={name}
                />

                <label class="block mt-4 text-sm font-medium">To (Receiver)</label>
                <input
                        class="w-full mt-1 p-2 border rounded"
                        type="text"
                        placeholder="e.g., Elon Musk"
                        bind:value={receiver}
                />

                <label class="block mt-4 text-sm font-medium">What’s your reply about? Key points:</label>
                <textarea
                        class="w-full mt-1 p-2 border rounded h-32"
                        placeholder="Write your reply key points here..."
                        bind:value={emailGoals}
                ></textarea>
            </div>
        {/if}

        <!-- Categories Section -->
        <div class="flex space-x-4 mt-6">
            {#each categories as category}
                <button
                        class={`py-2 px-4 rounded ${
                        activeCategory === category
                            ? "bg-purple-600 text-white"
                            : "bg-gray-200 text-gray-600"
                    }`}
                        on:click={() => setActiveCategory(category)}
                >
                    {category}
                </button>
            {/each}
        </div>

        <!-- Submit Button -->
        <button
                class="mt-6 w-full bg-purple-600 text-white py-2 rounded hover:bg-purple-700"
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
